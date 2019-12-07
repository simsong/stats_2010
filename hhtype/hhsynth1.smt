; -*- mode: lisp -*-
;; What can we do with HHTYPE to find satisfying solutions?

(declare-sort hhtype)
(declare-fun size (hhtype) Int)
(declare-fun multig (hhtype) Bool)
(declare-fun married (hhtype) Bool)
(declare-fun cohabiting (hhtype) Bool)
(declare-fun opposite-sex (hhtype) Bool)

; the household we are going to prototype
(declare-const h hhtype)
(assert (>= (size h) 1))
(assert (<= (size h) 7))

(declare-const h-size Int) (assert (= h-size (size h)))

(check-sat)
(get-model)



            
