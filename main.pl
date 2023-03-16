isfirstyear(Year):-Year=:=1,write("No electives available"),nl,nl,abort; Year>1,isSecondYear(Year),nl,nl.
isSecondYear(Year):-Year=:=2,findall(X,course(_,X,_,_,_,2,_),List1),write("Available courses:"),nl,
    print_list(List1),
    recursion(List1),abort;
    Year>2,isLastyear(Year).

isLastyear(Year):-year(Year),Year>2,Year<6,findall(Id,course(_,Id,_,_,_,3,_),List),recursion(List).

%mandatory courses
experiment:-
    findall(X,course(_,X,man,_,_,_,_),List2),write("Note mandatory courses for placement"),nl,print_list(List2),nl,nl.


print_list([]):-nl. %nl = newline
print_list([H|T]):-write(H),write(' , '),print_list(T).



import:-

    retractall(course(_,_,_,_,_,_,_)),
    csv_read_file('C:/Users/LEGION/Desktop/AI/data.csv', Data, [functor(course), seperator(0';)]),
    maplist(assert, Data).
    %findall(Id,course(_,Id,_,_,_,_,_),List),
    %recursion(List).

recursion([]).
recursion([H|T]):-increment(H),recursion(T).



increment(Id):-
    course(Name, Id, Field, Pre, Diff, Yr, Score),
    Score1 is Score+1,
   % writeln(Name), writeln(Score), writeln(Score1),
    retract(course(Name, Id, Field, Pre, Diff, Yr, Score)),
    assert(course(Name, Id, Field, Pre, Diff, Yr, Score1)).


main:-
    check,
    import,
    year(Year),
    isfirstyear(Year),
    nl,
    get_Interests,
    future_plan.

get_Interests:-

    interest(Interest),
    findall(X,course(_,X,Interest,_,_,_,_),Listnew),nl,
   recursion(Listnew).

future_plan:-
    plans(Plans),
    check_Plans(Plans).


check_Plans(Plans):- Plans=:=1,nl,experiment,ask_Gpa,
    nl;

    (Plans=:=2,nl,extra(Pj),ask_Projects(Pj)).


ask_Projects(Y):-
nl,nl, (Y == y ->projects);ask_Gpa.
    %(write('consider doing some projects and electives in  '),nl,nl, findall(X,course(_,X,_,_,_,_,2),List6),
   % print_list(List6)),abort.
projects:-
    projects(Done),
    (
    nl,nl,
    findall(X,course(_,X,Done,_,_,_,_),Listnew1)
    ),recursion(Listnew1),
             nl,ask_Gpa


    .

ask_Gpa:-
   gpa(G),check_Gpa(G).

check_Gpa(G):-G=:=1,writeln("Your GPA is fine! ")
    %,findall(X,course(_,X,_,_,_,_,3),List16),print_list(List16)
    ,prereq,!;
     writeln('You need to work on your GPA'),
     findall(K,course(_,K,_,_,easy,_,_),List8),
     recursion(List8),
    findall(X,course(_,X,_,_,_,_,4),List7),nl
    ,findall(X,course(_,X,_,_,_,_,3),List12),nl,
    write('Advice the following easier electives according to priority and the topic of your project:'),nl,

    print_list(List7)
    ,nl,
    print_list(List12),
    nl,prereq,
    abort .
prereq:-
    findall(X,course(_,_,_,X,_,_,4),List15),
    findall(X,course(_,_,_,X,_,_,3),List16),
    findall(X,course(_,_,_,X,_,_,2),List17),

    findall(Z,course(_,Z,_,_,_,_,4),List20),
    findall(Z,course(_,Z,_,_,_,_,3),List21),
    findall(Z,course(_,Z,_,_,_,_,2),List22),

    write("these are the recommended courses based on your inputs(priority wise) :"),nl,print_list(List20),print_list(List21),print_list(List22),nl,write("and their respective mandatory pre-requisites to be completed are"),nl,print_list(List15),print_list(List16),print_list(List17).

check:-
    consult("temp.pl")
    .


