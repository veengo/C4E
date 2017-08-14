using System;

namespace C7
{
	class MainClass
	{
		public static void Main (string[] args)
		{
			//decimal to binary 
			int value = 13;
			string binary = Convert.ToString (value, 2);
			Console.WriteLine (binary);
		}
			 
		}
	}
