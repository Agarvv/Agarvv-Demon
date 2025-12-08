
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#define BUFFER_SIZE 10

pthread_cond_t empty, full, sig; 
pthread_mutex_t mutex;
int buffer[BUFFER_SIZE];

void initbuffer() {
    for(int i = 0; i < BUFFER_SIZE;i++) {
       buffer[i] = 0; 
    }
}

// number of free items in the buffers
int buffcount()  {
    int empty = 0; 
    for(int i = 0; i < BUFFER_SIZE;i++) {
        printf("buffer[%d]: %d\n", i, buffer[i]);
       if(buffer[i] == 0 ){
         empty++; 
       }
    }

    return empty; 
}

int freeindex() {
    int index = 0; 

    for(int i = 0; i < BUFFER_SIZE; i++) {
      if(buffer[i] == 0) {
        index = i; 
      }
    }

    return index; 
}

int fullindex() {
    int index = 0;

    for(int i = 0; i < BUFFER_SIZE; i++) {
        if(buffer[i] != 0) {
            index = i;
        }
    }

    return index; 
}

void* producer() {
    while(1) {      
    pthread_mutex_lock(&mutex); 
    
    int freecount = buffcount(); 
    while(freecount == 0) {
        printf("buffer count: %d\n", freecount);
        printf("Buffer Already Full \n");
        pthread_cond_wait(&empty, &mutex); 
    }

    int index = freeindex(); 
    printf("index: %d\n", index);
    buffer[index] = 1;
    printf("Produced\n");
    pthread_cond_signal(&full);

      sleep(2);
    pthread_mutex_unlock(&mutex); 
  }

  return NULL;
}

void* consumer() {
    while(1) {     
        pthread_mutex_lock(&mutex); 
        int freecount = buffcount();

        while(freecount == BUFFER_SIZE) {
             printf("Buffer Already Empty\n");
            pthread_cond_wait(&full, &mutex); 
           
        }

        printf("cons ok\n");
        int fullind = fullindex();
        buffer[fullind] = 0;

        printf("Consumed\n");
        pthread_cond_signal(&empty);
        
        sleep(2);
        pthread_mutex_unlock(&mutex); 
    }

    return NULL;
}

int main() {
    initbuffer(); 
    pthread_cond_init(&empty, NULL);
    pthread_cond_init(&full, NULL);
    pthread_mutex_init(&mutex, NULL);
    pthread_t cons; 
    pthread_t prod; 
    
    pthread_create(&prod, NULL, producer, NULL); 
    pthread_create(&cons, NULL, consumer, NULL); 
    
    printf("Threads Created\n"); 
    
    pthread_join(cons, NULL); 
    
    
    printf("Finish");
    return 0;