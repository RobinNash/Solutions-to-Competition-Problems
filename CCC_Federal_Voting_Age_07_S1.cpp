//CCC Federal Voting Age 07 S1
//August 20, 2019
//By Robin Nash

#include<iostream>

using namespace std;

bool isEligible(int year, int month, int day){
	
	// exactly 18 years is 1989, 2, 27
	if (year > 1989)
		return false;
	if (year < 1989)
		return true;
	if (month > 2)
		return false;
	if (month < 2)
		return true;
	if (day > 27)
		return false;
	return true;
}

int main(){
	
	int dates;
	scanf("%d", &dates);
	
	for (int i=0;i<dates;i++){
		int year, month, day;
		scanf("%d %d %d", &year, &month, &day);
		if (isEligible(year,month,day))
			printf("%s\n", "Yes");
		else
			printf("%s\n", "No");	
		
	}
	
		
	return 0;
}
//1566326734.0