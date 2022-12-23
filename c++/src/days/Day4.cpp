#include <iostream>
#include <string>
#include <algorithm>

#include "Day4.h"
#include "../helpers/Reader.h"

Day4::Day4()
{
	//m_vecInput = ReadInput("../../../inputs/day4.txt");
	m_vecInput = ReadInput("../inputs/day4.txt");
}



int Day4::Part1(std::vector<std::string> sectionlist)
{
    std::vector<std::string>::iterator iter;
	int totalcount = 0;
	for(iter = sectionlist.begin(); iter < sectionlist.end(); iter++ )
	{   
		std::string sections = *iter;
		int sec1[2] = {0,0};
		int sec2[2] = {0,0};
		sec1[0] = stoi(sections.substr(0, sections.find("-")));
		sections = sections.substr(sections.find("-") + 1, sections.length());
		sec1[1] = stoi(sections.substr(0, sections.find(",")));
		sections = sections.substr(sections.find(",") + 1, sections.length());
		sec2[0] = stoi(sections.substr(0, sections.find("-")));
		sections = sections.substr(sections.find("-") + 1, sections.length());
		sec2[1] = stoi(sections.substr(0, sections.find(",")));
		sections = sections.substr(sections.find(",") + 1, sections.length());
		std::cout << sec1[0] << " " << sec1[1]<< " "<< sec2[0] << " " << sec2[1]<< std::endl;
		

	}
	return totalcount;
}

int Day4::Part2 (std::vector<std::string> sectionlist)
{
    std::vector<std::string>::iterator iter;
	int totalcount = 0;
	for(iter = sectionlist.begin(); iter < sectionlist.end(); iter++ )
	{   
	}
	
    return totalcount;
}

bool Day4::Solve()
{
	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}