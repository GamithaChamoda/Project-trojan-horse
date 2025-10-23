<?php
    include("connection.php");
    $sql = "SELECT id, exicutedResults FROM exicutedResults";
    $result = $conn->query($sql);
    include("authenticationChek.php");
    if($backendLoging != 1){

    }
    else{
        echo'<script>
                    window.location.href = "backend.php";
                    alert("Plese Login")
                </script>';
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #000;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>backendData</h1>
    <?php
    if ($result->num_rows > 0) {
        echo "<table>";
        echo "<tr><th>ID</th><th>Exicuted Results</th></tr>";

        // Output data of each row
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["id"]. "</td>";
            echo "<td>" . $row["exicutedResults"]. "</td>";
            echo "</tr>";
        }

        echo "</table>";
    } else {
        echo "No data found";
    }

    $conn->close();
    ?>
</body>
</html>





