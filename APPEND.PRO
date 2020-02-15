trace
domains
	list=symbol*
predicates
	app(list,list,list)
	g
clauses
	app([],L2,L2).
	app([H|T],L2,[H|R]):-
		app(T,L2,R).
		
	g:-
		app([a,b,c],[d,e],R),write(R),nl.
	g.
	