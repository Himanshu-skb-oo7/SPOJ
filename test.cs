using System;

public class Test
{
	public static void Main()
	{
		string number;
		while(true)
		{
			number = Console.ReadLine();
			if (number == "42")
				break;
			Console.WriteLine(number);
		}
	}
}
