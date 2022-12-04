#include <iostream>
#include <string>
#include "days\Day1.h"

int main(int argc,char* argv[])
{
	if(static_cast<std::string>(argv[1]) == "day1")
	{
		Day1 day = Day1();
	}
	return 0;
}
