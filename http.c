#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h> 

int main() {
    
    struct in_addr addr; 
    struct sockaddr_in myaddr;
    addr.s_addr = INADDR_ANY;

    myaddr.sin_port = htons(8080);
    myaddr.sin_addr = addr; 
    myaddr.sin_family = AF_INET;
    printf("IP en binario: %u\n", addr.s_addr);
     
    // create socket and bind it 
    int fd = socket(AF_INET, SOCK_STREAM, 0); 

    if(fd == -1) {
        perror("Error in socket creation");
    }
    
    int b = bind(fd, &myaddr, sizeof(myaddr));
    if(b == -1) {
       perror("Error in bind creation");
    }

    // google ip 142.251.39.206
    struct in_addr google_addr; 
    google_addr.s_addr = inet_addr("142.250.179.68"); 

    struct sockaddr_in g_address; 
    g_address.sin_addr = google_addr; 
    g_address.sin_port = htons(80); 
    g_address.sin_family = AF_INET; 

    int con = connect(fd, &g_address, sizeof(g_address));

    if(con == -1) {
        perror("Error while connecting to google \n");
    }


    
    printf("Socket fd: %d\n", fd); 
    printf("Connected to google\n");
    

    // Después del connect exitoso
    char* http_request = "GET / HTTP/1.1\r\n"
                     "Host: google.com\r\n"
                     "Connection: close\r\n"
                     "\r\n";

    write(fd, http_request, strlen(http_request));
    
    char bytes[4096];

    read(fd, bytes, sizeof(bytes));

    printf("bytes %s \n", bytes); 

    return 0; 
}