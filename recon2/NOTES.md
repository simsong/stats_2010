PCT12J.
SEX BY AGE (BLACK OR AFRICAN AMERICAN ALONE, NOT HISPANIC OR LATINO) [209]—Con.
PCT012J071:  

blackmale68(p) = (black(p)+male(p)+age(p)=70) AND (age(p)=68)

bm68(p1) + bm68(p2) + bm68(p3) + bm68(p4) = 1

bm68(p1) xor bm68(p2) xor bm6(p
avoids the If.

(declare-fun black (p) Int) 
(declare-fun male (p) Int) 
(declare-fun age (p) Int) 


(declare-sort person)
(declare-const p1 person)
(declare-const p2 person)
(declare-fun black (person) Int)

(declare-fun blackmale68 ((p person)) Int
             (ite (and (= (+ (black p) (male p) (age p) 70))
                       (= (age p) 68)) 1 0))

(assert (= (+ (blackmale68 p1) (blackmale68 p2) (blackmale68 p3) (blackmale68 p4)) 1))
             
;; ites are slow. TOo many variables. Takes a long time to propigate informaiton.



Person1black = 0,1
Person1white = 0,1
Person1asian = 0,1
Person1hawaiin
Person1SomeOtherRace
Person1Age = 0..115
Person1Hispanic = 0, 1
Person1Sex = 0, 1

