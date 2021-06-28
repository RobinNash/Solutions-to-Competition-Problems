//CCC Its Cold Here 08 S1
//August 20, 2019
//By Robin Nash

#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main(){

	map<int, string> cities{};
	
	int temperature = 201;
	
	
	while(true){
		int temp;
		string city, line;
		
		getline(cin, line);

		
		size_t space = line.find(" ");
		
		city = line.substr(0,space);
		temp = stoi(line.substr(space));
		
		cities[temp] = city;
		
		if (temp < temperature)
			temperature = temp;
		
		if (city == "Waterloo")
			break;

	}
	
	string city = cities[temperature];
	
	cout << city;
	//printf("%s", city);
	
		
	return 0;
}
//1566328934.0