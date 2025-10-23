<?php
        include("connection.php");
        $exicutedResults = $_POST['exicutedResults'];

        $sql = "INSERT INTO exicutedResults (exicutedResults) VALUES ('$exicutedResults')";
        $result = mysqli_query($conn, $sql);
        header("Location:welcome.php");
    
?>