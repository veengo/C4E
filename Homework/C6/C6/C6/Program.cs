using System;

namespace C6
{
	class MainClass
	{
		public static void Main (string[] args)
		{

			{
				//Ex1
				Console.WriteLine ("What's your weight?");
				float weight = float.Parse (Console.ReadLine ());
				Console.WriteLine ("What's your height? ");
				float height = float.Parse (Console.ReadLine ()) / 100;
				float bmi = weight / (height * height);
				Console.WriteLine ("Yours Body Mass Index is " + bmi.ToString ("0.00"));
				if (bmi <= 16) {
					Console.WriteLine ("You're severely underweighted");
				} else if (bmi <= 18) {
					Console.WriteLine ("You're underweighted");
				} else if (bmi < 25) {
					Console.WriteLine ("You're normal");
				} else if (bmi < 30) {
					Console.WriteLine ("You're overweight");
				} else {
					Console.WriteLine ("You're obese");
				}
				Console.ReadLine ();

				//Ex2
				Console.WriteLine ("Hello, ");
				Console.WriteLine ("my name ");
				Console.WriteLine ("is B-max");
				Console.ReadLine ();

				//Ex3
				//3.1

				int column = 10;
				int row = 10;
				for (int i = 0; i < column; i++) {
					Console.Write ("* ");
				}

				Console.WriteLine ();
				//3.2
				for (int i = 0; i < column; i++) {
					Console.Write ("x ");
					Console.Write ("* ");
				}

				Console.WriteLine ();

				//3.3
				for (int i = 0; i < row; i++) {
					for (int k = 0; k < column; k++) {
						if (i % 2 == 0) {
							Console.Write ("x*");
						} else {
							Console.Write ("*x");
						}
					}
					Console.WriteLine ();

				}
			}
		}
	}
}

