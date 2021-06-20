//CCC Icon Scaling 12 J3
//July 16, 2019
//By Robin Nash

#include <iostream>
#include <string>

using namespace std;

int main()
{
	string line;
	
	int k;
	scanf("%d", &k);
	
	for (int i=0; i<3; i++)
	{
		if (i==0)
			line = "*x*";
		else if (i==1)
			line = " xx";
		else
			line = "* *";
		
		// print line k times
		for (int i=0; i<k; i++){
			// select character
			for (char ch : line){
				//print charachter k times
				for (int i=0; i<k; i++){
					printf("%c", ch);
				}
			}
			printf("%s", "\n");
		}
		
		
	}
	return 0;
}
//1563312310.0