$(document).ready(function() {

    $("#addRecipe").click(function() {
        $("#form1").text($("form").serialize());
    });



    $('#addIngredient1Button').click(function() {
        $('#divIngredient2').show();
        $('input[name=ingredient2]').focus();
    })

    $('#ing2').click(function() {
        $('#div-ing3').show();
        $('input[name=ing3]').focus();
    })

    $('#ing3').click(function() {
        $('#div-ing4').show();
        $('input[name=ing4]').focus();
    })

    $('#ing4').click(function() {
        $('#div-ing5').show();
        $('input[name=ing5]').focus();
    })

    $('#ing5').click(function() {
        $('#div-ing6').show();
        $('input[name=ing6]').focus();
    })

    $('#ing6').click(function() {
        $('#div-ing7').show();
        $('input[name=ing7]').focus();
    })

    $('#ing7').click(function() {
        $('#div-ing8').show();
        $('input[name=ing8]').focus();
    })

    $('#ing8').click(function() {
        $('#div-ing9').show();
        $('input[name=ing9]').focus();
    })

    $('#ing9').click(function() {
        $('#div-ing10').show();
        $('input[name=ing10]').focus();
    })

    $('#ing10').click(function() {
        $('#div-ing11').show();
        $('input[name=ing11]').focus();
    })

    $('#ing11').click(function() {
        $('#div-ing12').show();
        $('input[name=ing12]').focus();
    })

    $('#ing12').click(function() {
        $('#div-ing13').show();
        $('input[name=ing13]').focus();
    })

    $('#ing13').click(function() {
        $('#div-ing14').show();
        $('input[name=ing14]').focus();
    })

    $('#ing14').click(function() {
        $('#div-ing15').show();
        $('input[name=ing15]').focus();
    })

    $('#ing15').click(function() {
        $('#div-ing16').show();
        $('input[name=ing16]').focus();
    })

    $('#ing16').click(function() {
        $('#div-ing17').show();
        $('input[name=ing17]').focus();
    })

    $('#ing17').click(function() {
        $('#div-ing18').show();
        $('input[name=ing18]').focus();
    })

    $('#ing18').click(function() {
        $('#div-ing19').show();
        $('input[name=ing19]').focus();
    })

    $('#ing19').click(function() {
        $('#div-ing20').show();
        $('input[name=ing20]').focus();
    })

    // Click the add button below Method>Step 1 to open text area for Method>Step 2 and focus cursor to the revealed section
    $('#step1btn').click(function() {
        $('#div-step2').show();
        $('#step2').focus();
    })

    // Click the add button below Method>Step 1 to open text area for Method>Step 2 and focus cursor to the revealed section
    $('#step2btn').click(function() {
        $('#div-step3').show();
        $('#step3').focus();
    })

    // Click the add button below Method>Step 3 to open text area for Method>Step 4 and focus cursor to the revealed section
    $('#step3btn').click(function() {
        $('#div-step4').show();
        $('#step4').focus();
    })
});