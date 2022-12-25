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

		std::vector<int> section1;
		std::vector<int> section2;
		int tempmin = 0;
		int tempmax = 0;
		if(sec1[0]>sec1[1])
		{
			tempmin = sec1[1];
			tempmax = sec1[0];
		}
		else
		{
			tempmin = sec1[0];
			tempmax = sec1[1];
		}
		for(int i = tempmin; i <= tempmax; i++)
		{
			section1.push_back(i);
		}
		
		if(sec2[0]>sec2[1])
		{
			tempmin = sec2[1];
			tempmax = sec2[0];
		}
		else
		{
			tempmin = sec2[0];
			tempmax = sec2[1];
		}
		for(int i = tempmin; i <= tempmax; i++)
		{
			section2.push_back(i);
		}
		
		std::vector<int>::iterator iter2;
		int findcount = 0;
		for(iter2 = section1.begin(); iter2 < section1.end(); iter2++ )
		{
			if(std::find(section2.begin(), section2.end(), *iter2) != section2.end())
			{
				findcount += 1;
			}
		}
		if(findcount == section1.size())
		{
			totalcount += 1;
		}
		if(section1.size() != section2.size())
		{

			findcount = 0;
			for(iter2 = section2.begin(); iter2 < section2.end(); iter2++ )
			{
				if(std::find(section1.begin(), section1.end(), *iter2) != section1.end())
				{
					findcount += 1;
				}
			}
			if(findcount == section2.size())
			{
				totalcount += 1;
			}
		}
	}
	return totalcount;
}

int Day4::Part2 (std::vector<std::string> sectionlist)
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

		std::vector<int> section1;
		std::vector<int> section2;
		int tempmin = 0;
		int tempmax = 0;
		if(sec1[0]>sec1[1])
		{
			tempmin = sec1[1];
			tempmax = sec1[0];
		}
		else
		{
			tempmin = sec1[0];
			tempmax = sec1[1];
		}
		for(int i = tempmin; i <= tempmax; i++)
		{
			section1.push_back(i);
		}
		
		if(sec2[0]>sec2[1])
		{
			tempmin = sec2[1];
			tempmax = sec2[0];
		}
		else
		{
			tempmin = sec2[0];
			tempmax = sec2[1];
		}
		for(int i = tempmin; i <= tempmax; i++)
		{
			section2.push_back(i);
		}
		
		std::vector<int>::iterator iter2;
		bool isfound = false;
		for(iter2 = section1.begin(); iter2 < section1.end(); iter2++ )
		{
			auto result1 = std::find(section2.begin(), section2.end(), *iter2);
			if(result1 != section2.end())
			{
				isfound = true;
			}
		}
		if(isfound)
		{
			totalcount += 1;
		}
	}
	return totalcount;
}

bool Day4::Solve()
{
	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}