
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <concord/discord.h>


int main() {
    struct discord *client = discord_init(getenv("DISCORD"));
    
    //discord_set_on_ready(client, &on_ready);
   // discord_set_on_interaction_create(client, &on_interaction);
    //discord_run(client);
}