#include <iostream>
#include <string>
#include "days\Day1.h"
#include "days\Day2.h"
#include "days\Day3.h"

int main(int argc,char* argv[])
{
	if(argc <= 1)
	{
		std::cout << "Please pass day as an argument!" << std::endl;
		return 0;
	}
	auto inputarg = static_cast<std::string>(argv[1]);
	if(inputarg == "day1")
	{
		Day1 day = Day1();
		day.Solve();
	}
	else if(inputarg == "day2")
	{
		Day2 day = Day2();
		day.Solve();
	}
	else if(inputarg == "day3")
	{
		Day3 day = Day3();
		day.Solve();
	}
	else
	{
		std::cout << "Please make sure your day input is correct!" << std::endl;
	}
	return 0;
}
