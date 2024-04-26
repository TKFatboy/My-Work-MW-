<!doctype html>
<html lang="en">

<head>
    <?php
    $page = "index";
    include "htmlhead.php";
    ?>
</head>

<body>
    <div class="container bg-light p-2 my-2">
        <?php
        include "pageheader.php";
        include "navbar.php";
        ?>

        <div class="row my-2 p-3">
            <div class="col-md-6">
                <img src="images/game.jpg" class="img-fluid img-thumbnail mx-auto d-block my-2" alt="" width="80%">
            </div>
            <div class="col-md-6">
                <h3>TK Company จำกัด</h3>
                <hr>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa placeat reiciendis vero temporibus!
                    Recusandae quam animi alias deserunt, provident dolores commodi laboriosam fuga omnis nostrum
                    pariatur voluptates eius unde dolore.</p>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum assumenda accusamus tempore ab quo
                    adipisci, repellendus nesciunt ea rerum, earum aliquid nobis quaerat, sequi laboriosam veritatis
                    porro reiciendis asperiores dolor.</p>
            </div>

        </div>

        <?php
        include "footer.php";
        ?>


    </div>



</body>

</html>