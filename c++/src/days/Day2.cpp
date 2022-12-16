#include <iostream>
#include <string>
#include <algorithm>

#include "Day2.h"
#include "../helpers/Reader.h"

Day2::Day2()
{
	//m_vecInput = ReadInput("../../../inputs/day2.txt");
	m_vecInput = ReadInput("../inputs/day2.txt");
}

int Day2::Part1(std::vector<std::string> hands)
{
    std::vector<std::string>::iterator iter;
    int totalscore = 0;
	for(iter = hands.begin(); iter < hands.end(); iter++ )
	{   
        int hand = 0;
        int comp = 0;
        if(iter->at(0) == 'A')
        {
            comp = 1;
        }
        
        if(iter->at(0) == 'B')
        {
            comp = 2;
        }
        
        if(iter->at(0) == 'C')
        {
            comp = 3;
        }
        
        if(iter->at(2) == 'X')
        {
            hand = 1;
            totalscore += hand;
        }
        
        if(iter->at(2) == 'Y')
        {
            hand = 2;
            totalscore += hand;
        }
        
        if(iter->at(2) == 'Z')
        {
            hand = 3;
            totalscore += hand;
        }

        if( (comp == 1 && hand == 2) || (comp == 2 && hand == 3) || (comp == 3 && hand == 1))
        {
            totalscore += 6;
        }
        if( (comp == 3 && hand == 2) || (comp == 1 && hand == 3) || (comp == 2 && hand == 1))
        {
            totalscore += 0;
        }
        if( (comp == 2 && hand == 2) || (comp == 3 && hand == 3) || (comp == 1 && hand == 1))
        {
            totalscore += 3;
        }

	}
    return totalscore;
}

int Day2::Part2(std::vector<std::string> hands)
{
	return 0;
}

bool Day2::Solve()
{
	std::cout << Part1(m_vecInput) <<std::endl;
	std::cout << Part2(m_vecInput) <<std::endl;
	return true;
}