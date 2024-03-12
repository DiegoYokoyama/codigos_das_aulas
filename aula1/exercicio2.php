<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>exercicio 1</title>
</head>
<body>
    <?php
    
    $val1=10;
    $val2=10;
    $val3=10;
    $media = ($val1 + $val2 + $val3)/3;

    // echo"A media é ".$media."<br>";
    $situacao=$media>=7?"Aprovado":"Reprovado";
    $situacao2=$media==10?" com distinção":" ";

    echo"a media: $media<br> Situação: $situacao $situacao2<br>";

    ?>
</body>
</html>