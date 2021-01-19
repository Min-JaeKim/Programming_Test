package com.ssafy.algo;

import java.util.Scanner;

public class DigitTest1 {

	public static void main(String[] args) {
		
		Scanner si = new Scanner(System.in);
		int count = si.nextInt();
		int[] num = new int[9];
		while (count != 0) {
			num[count/10] += 1;
			count = si.nextInt();
		}
		for (int i = 0; i < num.length; i++) {
			if(num[i] != 0)
				System.out.println(i + " : " + num[i] + "°³");
		}

}
}
