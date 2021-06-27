//CCC Cool Numbers 09 S1
//August 20, 2019
//By Robin Nash

#include<iostream>

using namespace std;

int main(){
	
	int a,b;
	scanf("%d\n%d", &a,&b);
	
	int cools[] = {1,64,729,4096,15625,46656,117649,262144,531441,1000000,1771561,2985984,
        4826809,7529536, 11390625, 16777216, 24137569, 34012224, 47045881,
		64000000, 85766121};
	
	int total = 0;
	for (int x : cools){
		if ( a <= x && x <= b)
			total ++;
			
		if ( x > b )
			break;
	}
	
	printf("%d", total);
	
		
	return 0;
}
//1566326048.0