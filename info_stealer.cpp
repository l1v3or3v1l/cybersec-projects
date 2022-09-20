#include <iostream>
#include <winsock.h>
#include <fstream>
#include <string>
using namespace std;

struct sockaddr_in srv;

int main() {

	const char* FILENAME = "file.txt";    // change

	ifstream f (FILENAME);

	string data ( (istreambuf_iterator<char>(f) ),
				  (istreambuf_iterator<char>()  ) );
	
	WSADATA ws;
	WSAStartup(MAKEWORD(2, 2), &ws);
	
	const char* IP = "127.0.0.1";    // change
	int PORT = 8080;                  // change
	int sock = socket(AF_INET, SOCK_STREAM, 0);

	srv.sin_family = AF_INET;
	srv.sin_addr.s_addr = inet_addr(IP);
	srv.sin_port = htons(PORT);

	connect(sock, (sockaddr*)&srv, sizeof(srv));
	send(sock, data.c_str(), data.length(), 0);

	return 0;

}