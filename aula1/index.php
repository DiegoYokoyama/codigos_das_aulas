<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>php</title>
</head>
<body>

<h1>Meu Primeiro Código PHP</h1>

<?php
echo"Olá Senac!<br>";

$num1=10;
$num2=20;
$soma= $num1+$num2;
echo"A Soma de $num1+$num2=$soma<br>";

/* funções */

$x = 35.52;
$z = -40;


Abs($z); #Tranforma em um valor absoluto.
Pow($x,2); #Potenciação.
Sqrt($x); #Raiz quadrada.
Round($x); #Arredonda.
Intval($x); #Pega o numero inteirol.
Number_format($x,2,",","."); #Substitui o ultimo simbolo informado pelo primeiro. Altera as casas decimais.


#vetores 

$nota=[]; //inicio do vetor
$nota[1]=7;
$nota[2]=6;
$nota[3]=7;
$nota[4]=6;

echo"A Nota 1 é = $nota[1]<br>";
$media = ($nota[1] + $nota[2] + $nota[3] + $nota[4])/4;

echo"A media é ".$media."<br>";
$situacao=$media>=6?"Aprovado":"Reprovado";

echo"Situação".$situacao."<br>";

//while

/*$i = 0;
do{
    echo $i;
    $i++;
}while ($i <= 10);

//for

for($i=1; $<=10; $i++){
    echo $i;
}
*/

?>

</body>
</html>