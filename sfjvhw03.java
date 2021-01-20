package com.ssafy.algo;

import java.util.Scanner;

public class hwjava03_10_±ËπŒ¿Á {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int test = sc.nextInt();
		int[] result = new int [test];
		for(int i = 0; i < test; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			boolean[][] arr = new boolean [a][a];
			int count = b;
			
			
			for(int j = 0; j < b; j++) {
				int col = sc.nextInt();
				int row = sc.nextInt();
				int move = sc.nextInt();
				
				
				if(move == 1) {
					if(col-6 < 0 || arr[col-6][row]) {
						count--;
						continue;
					}
					arr[col-6][row] = true;
				}
				else if (move == 2) {
					if(col+6 > a-1 || arr[col+6][row]) {
						count--;
						continue;
					}
					arr[col+6][row] = true;
				}
				else if (move == 3) {
					if(row-6 < 0 || arr[col][row-6]) {
						count--;
						continue;
					}
					arr[col][row-6] = true;
				}
				else {
					if(row+6 > a-1 || arr[col][row+6]) {
						count--;
						continue;
					}
					arr[col][row+6] = true;
				}
			}
			result[i] = count;
		}
		
		for(int i = 0; i < result.length; i++)
			System.out.println("#" + (i+1)  + " : " + result[i]);

	}

}
