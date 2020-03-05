% def TowerOfHanoi(n , from_rod, to_rod, aux_rod): 
%     if n == 1: 
%         print "Move disk 1 from rod",from_rod,"to rod",to_rod 
%         return
%     TowerOfHanoi(n-1, from_rod, aux_rod, to_rod) 
%     print "Move disk",n,"from rod",from_rod,"to rod",to_rod 
%     TowerOfHanoi(n-1, aux_rod, to_rod, from_rod) 
%           
% # Driver code 
% n = 4
% TowerOfHanoi(n, 'A', 'C', 'B')  

trace

predicates
	toh(integer,symbol,symbol,symbol)
	g
clauses
	toh(N,F,T,A):-
		N = 1,
		write("1 ",F," ",T),nl,!;
		N1 = N-1, toh(N1, F, A, T),
		write(N," ",F," ",T),nl,
		toh(N1, A, T, F),!.
	g:-toh(3,a,c,b).