$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('#btn-predict').show();
                $('#result').fadeIn(600);
                // Parse JSON response and display prediction with confidence
                // Handle both JSON object and string responses
                var prediction, confidence;
                if (typeof data === 'string') {
                    // If response is a string, try to parse it
                    try {
                        data = JSON.parse(data);
                    } catch(e) {
                        // If parsing fails, use the string as prediction
                        $('#result').text('Result: ' + data);
                        console.log('Success!', data);
                        return;
                    }
                }
                // Extract prediction and confidence from JSON object
                prediction = data.prediction || 'Unknown';
                confidence = data.confidence ? (data.confidence * 100).toFixed(2) + '%' : '';
                var resultText = 'Result: ' + prediction;
                if (confidence) {
                    resultText += ' (Confidence: ' + confidence + ')';
                }
                $('#result').text(resultText);
                console.log('Success!', data);
            },
            error: function (xhr, status, error) {
                $('.loader').hide();
                $('#btn-predict').show();
                $('#result').fadeIn(600);
                var errorMsg = 'Error: ' + error;
                if (xhr.responseText) {
                    try {
                        var errorData = JSON.parse(xhr.responseText);
                        errorMsg = errorData.error || errorMsg;
                    } catch(e) {
                        errorMsg += ' - ' + xhr.responseText;
                    }
                }
                $('#result').text(errorMsg);
                console.log('Error:', error, xhr.responseText);
            }
        });
    });

});
