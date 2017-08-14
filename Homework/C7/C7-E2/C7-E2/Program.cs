using System;

namespace C7E2
{
	class MainClass
	{

			public static void Main (string[] args)
			{
			int a,b;
			a = 7;
			b = 9;
			i = (a > b) ? a : b;
			int GCD = 1;
			for (int j = 1; j <= i; j++) {
				if (a % j == 0 && b % j == 0) {
					GCD = j;
				}
				Console.WriteLine (GCD);
			}
		}
	}
