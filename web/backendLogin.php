<?php
    include("connection.php");
    if(isset($_POST["submit"])){
        if(isset($_POST['submit'])){
            $username = $_POST['user'];
            $password = $_POST['pass'];

            $sql = "select * from admin where username = '$username' and password = '$password'";
            $result = mysqli_query($conn, $sql);
            $row = mysqli_fetch_array($result, MYSQLI_ASSOC);
            $count = mysqli_num_rows($result);
        if($count == 1){
            include("authenticationChek.php");
            $backendLoging = 1;
            header("Location:backendData.php");
        }
        else{
            echo'<script>
                    window.location.href = "backend.php";
                    alert("error")
                </script>';
        }
        
    }

    }
    else{
        echo '<script>
            window.location.href = "backend.php";
            alert("error")
            </script>';
    }
    
?>