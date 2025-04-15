#include <arpa/inet.h>
#include <netdb.h>
#include <stdio.h>
#include <stdlib.h> // For exit()
#include <string.h>
#include <strings.h>
#include <sys/socket.h>
#include <unistd.h>

#define MAX 80
#define PORT 8080
#define SA struct sockaddr

void func(int sockfd)
{
    char buff[MAX];
    int n;

    for (;;)
    {
        bzero(buff, sizeof(buff));
        printf("Enter the string: ");
        n = 0;

        // Read input from user
        while ((buff[n++] = getchar()) != '\n')
            ;

        // Send to server
        write(sockfd, buff, sizeof(buff));

        // Clear buffer and read from server
        bzero(buff, sizeof(buff));
        read(sockfd, buff, sizeof(buff));

        printf("From server: %s", buff);

        if ((strncmp(buff, "Exit", 4)) == 0)
        {
            printf("Client Exit...\n");
            break;
        }
    }
}

int main()
{
    int sockfd;
    struct sockaddr_in servaddr;

    // Socket creation
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1)
    {
        printf("Socket creation failed...\n");
        exit(0);
    }
    else
    {
        printf("Socket successfully created..\n");
    }

    bzero(&servaddr, sizeof(servaddr));

    // Server info
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(PORT);

    // Connect to server
    if (connect(sockfd, (SA *)&servaddr, sizeof(servaddr)) != 0)
    {
        printf("Connection with the server failed...\n");
        exit(0);
    }
    else
    {
        printf("Connected to the server...\n");
    }

    func(sockfd);

    close(sockfd);
}
