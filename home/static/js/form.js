$(function() {
  var csrftoken = getCookie("csrftoken");

  function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    console.log(unindexed_array)
    var indexed_array = {};

    $.map(unindexed_array, function(n, i) {
      indexed_array[n["name"]] = n["value"];
    });

    return indexed_array;
  }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      var cookies = document.cookie.split(";");
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  $("#addProduct").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "/add_product/",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#addProduct").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#addProduct").hide();
          $("#addProduct").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse .response").html(
            "<p > " +
              "Successfully added new product" +
              "</p>")
        //   $("#sendInquiryResponse").html(
        //     "<p>" + response.error.message + "</p>"
        //   );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  })
  $("#sellProduct").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "/handle_product_sale/",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#sellProduct").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#sellProduct").hide();
          $("#sellProduct").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse .response").html(
            "<p > " +
              "Successfully added new product" +
              "</p>")
        //   $("#sendInquiryResponse").html(
        //     "<p>" + response.error.message + "</p>"
        //   );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  })
  
  $("#addShelf").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "/addShelf/",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#addShelf").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#addShelf").hide();
          $("#addShelf").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse .response").html(
            "<p > " +
              "Successfully added new New Shelf" +
              "</p>")
        //   $("#sendInquiryResponse").html(
        //     "<p>" + response.error.message + "</p>"
        //   );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  })
  $("#addClient").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "/addClient/",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#addClient").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#addClient").hide();
          $("#addClient").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse .response").html(
            "<p > " +
              "Successfully added new client" +
              "</p>")
        //   $("#sendInquiryResponse").html(
        //     "<p>" + response.error.message + "</p>"
        //   );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  })

    $("#addRent").submit(function(e) {
    e.preventDefault();
    var form = $(this);
    var data = getFormData(form);
    console.log(data);
    $.ajax({
      type: "POST",
      contentType: "application/json",
      url: "/addRent/",
      headers: {
        "X-CSRFToken": csrftoken
      },
      data: JSON.stringify(data),
      success: function(response, status) {
        if (response.error) {
          $("#addRent").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse").html(
            "<p>" +
              "Error occured, kindly contact us on the live chat on the bottom right corner" +
              "</p>"
          );
          console.log(response.error);
        } else {
          console.log("success");
          $("#addRent").hide();
          $("#addRent").hide();
          $("#sendInquiryResponse").css("display", "block");
          $("#sendInquiryResponse").css("background-color", "red !important");
          $("#sendInquiryResponse .response").html(
            "<p > " +
              "Successfully added new Rent Payment" +
              "</p>")
        //   $("#sendInquiryResponse").html(
        //     "<p>" + response.error.message + "</p>"
        //   );
        }
      },
      error: function(response, error) {
        console.log(response);
        console.log(status);
      }
    });
  })
  ;})
  ;