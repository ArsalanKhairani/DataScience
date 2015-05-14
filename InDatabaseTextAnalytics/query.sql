/*
SELECT MAX(sumCount)
FROM (
	SELECT FA.docid, FA.term, FB.docid, FB.term, SUM(FA.count) AS sumCount
	FROM newFrequency FA, newFrequency FB
	WHERE FB.docid = 'q' AND FA.docid <> 'q' AND FA.term = FB.term
	GROUP BY FA.docid
);

SELECT FA.docid, FA.term, FB.docid, FB.term, SUM(FA.count * FB.count)
FROM frequency FA, frequency FB
WHERE FA.docid = '10080_txt_crude' AND FB.docid = '17035_txt_earn' AND FA.term = FB.term;

SELECT A.row_num, B.col_num, sum(A.value * B.value)
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY A.row_num, B.col_num;

SELECT count(*) 
FROM (
	SELECT SUM(count)
	FROM frequency
	GROUP BY docid
	HAVING SUM(count) > 300
) x;

SELECT count(*) 
FROM (
	SELECT DISTINCT docid
	FROM (
		SELECT docid
		FROM frequency
		WHERE term = "transactions"
		INTERSECT
		SELECT docid
		FROM frequency
		WHERE term = "world"
	)
) x;

SELECT count(*) 
FROM (
	SELECT *
	FROM frequency
	WHERE term = "parliament"
) x;

SELECT count(*) 
FROM (
	SELECT term
	FROM frequency 
	WHERE docid = "10398_txt_earn" AND count = 1
	UNION
	SELECT term
	FROM frequency 
	WHERE docid = "925_txt_trade" AND count = 1
) x;

SELECT count(*) 
FROM (
	SELECT term 
	FROM frequency 
	WHERE docid = "10398_txt_earn" AND count = 1
) x;

SELECT count(*) 
FROM (
	SELECT * 
	FROM frequency 
	WHERE docid = "10398_txt_earn"
) x;
*/