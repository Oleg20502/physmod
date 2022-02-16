// uniform_int_distribution::operator()
#include <iostream>
#include <chrono>

#include <random>
#include <functional>

#include <iomanip>
#include <map>

int main(int argc, char** argv)
{
	if (argc != 2){
		return 1;
	}
	int max_N = std::atoi(argv[1]);

	std::random_device rd{};
	std::mt19937 gen{rd()};

	std::normal_distribution<> d{0,1};
	auto gauss52 = std::bind(d, gen);

	for(int n=0; n<max_N; ++n) {
	 std::cout << gauss52() << std::endl;
	}
  			

  return 0;
}