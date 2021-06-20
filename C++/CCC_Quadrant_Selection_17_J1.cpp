//CCC Quadrant Selection 17 J1
//July 16, 2019
//By Robin Nash

#include <iostream>

using namespace std;

int main(){
	int x, y, q;
	scanf("%d", &x);
	scanf("%d", &y);
	
	if (x<0)
		if (y<0)
			q = 3;
		else
			q = 2;
	else
		if (y<0)
			q = 4;
		else
			q = 1;
	
	printf("%d", q);
	return 0;
}

//1563312978.0