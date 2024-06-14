# Dynamic Programming and Greedy Algorithms

## Solving Recurrence

$$
\begin{align*}
n \ &-> n/b \  -> O_1  \ \ -> O \\
&-> n/b \ -> O_2   \ \ -> \\
&-> n/b \ -> O_3   \ \ -> \\
&-> n/b \ -> O_4   \ \ -> 
\end{align*}
$$

$$
T(n) = 
\begin{cases}
\Theta(1), \ \text{if $n \le 1$}\\ \\
aT(\frac{n}{b}) + f_{div}(n) + f_{comb}(n)
\end{cases}
$$


$$
MergeSort \\
a = 2, b = 2 \\\\
f_{div}(n) : \Theta(1), \ f_{comb}(n) : \Theta(n) \\\\
T(n) = 
\begin{cases}
\Theta(1), \ \text{if \ $n \le 1$} \\\\
2T(\frac{n}{2}) + \Theta(n)
\end{cases}
$$

$$
Karatsuba's \ Algorithm \\\\
\begin{cases}
a_1b_1 \\
a_2b_2 \\
(a_1 + a_2)(b_1 + b_2) 
\end{cases} 
\rightarrow a \times b \\\\
f_{div}, \ addition, \ substraction, \ padding : \Theta(n) \\\\
T(n) = 
\begin{cases}
\Theta(1), \ \text{if $n \le 1$} \\
3T(\frac{n}{2}) + \Theta(n), \ O.W.
\end{cases}
$$


$$

$$

$$
Solving \ Recurrence \\\\
T(n) = 
\begin{cases}
C_0, \ \text{if $n \le 1$} \\
2T(\frac{n}{2}) + C_1n, \ O.W.
\end{cases} \\\\
$$

### Expansion Method

$$
Expansion \ Method \\\\
\begin{align*}
T(n) &= 2T(\frac{n}{2}) + C_1n \\
		 &= 2[2T(\frac{n}{4}) + C_1\frac{n}{2}] + C_1n \\
		 &= 2^2T(\frac{n}{2^2}) + 2 \cdot C_1\frac{n}{2}  + C_1n \\
		 &= 2^2[2T(\frac{n}{2^3}) + C_1(\frac{n}{2^2})] + 2C_1n \\
		 &= 2^3T(\frac{n}{2^3}) + 3C_1n \leftarrow  \text{3 expansion} \\
		 &= 2^4T(\frac{n}{2^4}) + 4C_1n \leftarrow  \text{4 expansion} \\
		 &= 2^jT(\frac{n}{2^j}) + jC_1n \leftarrow  \text{j expansion} \\
		 &= 2^j T(1) + jC_1n \\
		 &= 2^{\log_2n}C_0 + (\log_2n)C_1n \\
		 &= C_0n + (\log_2n)C_1n \\
		 &=\Theta(n \log n)
\end{align*} \\
\frac{n}{2^j} = 1 \rightarrow j = \log_2n
$$

### Master Method

$$
Master \ Method \\\\
T(n) = 
\begin{cases}
\Theta(1), \ \text{if $n \le 1$} \\
aT(\frac{n}{b})+ \Theta(n^c), \ O.W.
\end{cases} \\\\

\begin{cases}
\log_ba > c \rightarrow T(n) = \Theta(n^{\log_ba}) \\
\log_ba = c \rightarrow T(n) = \Theta((n^{\log_ba})\log{n}) \\
\log_ba < c \rightarrow T(n) = \Theta(n^c) \\
\end{cases} \\\\
Kabatsuba : T(n) = 3T(\frac{n}{2}) + \Theta(n^1) \\
\log_ba = \log_23 > 1 = c\rightarrow \Theta(n^{\log_23}) \\\\
Graduate \ School : T(n) = 4T(\frac{n}{2}) + \Theta(n^1) \\
\log_ba = \log_24 > 1 = c\rightarrow \Theta(n^{\log_24}) \\\\
Strassen : T(n) = 7T(\frac{n}{2}) + \Theta(n^2) \\
\log_ba = \log_27 > 2 = c\rightarrow \Theta(n^{\log_27}) \\\\
$$



 



















