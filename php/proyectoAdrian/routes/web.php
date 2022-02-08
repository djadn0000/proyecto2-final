<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('auth.login');
});

Route::get('/admin', function () {
    return view('admin.index');
});

Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::get('blacklists', [App\Http\Controllers\BlackListController::class, 'index']);
Route::get('blacklists/create', [App\Http\Controllers\BlackListController::class, 'create']);
Route::post('blacklists/store', [App\Http\Controllers\BlackListController::class, 'store']);
Route::patch('blacklists/update/{id}', [App\Http\Controllers\BlackListController::class, 'update']);
Route::delete('blacklists/{id}', [App\Http\Controllers\BlackListController::class, 'destroy']);
Route::get('blacklists/{id}/edit', [App\Http\Controllers\BlackListController::class, 'edit']);

Route::get('user', [App\Http\Controllers\UserController::class, 'index']);
Route::get('user/{id}', [App\Http\Controllers\UserController::class, 'show']);
Route::patch('user/update/{id}', [App\Http\Controllers\UserController::class, 'update']);
Route::get('user/{id}/edit', [App\Http\Controllers\UserController::class, 'edit']);


    /*->missing(function (Request $request) {
        return Redirect::route('blacklists.index');
    });*/
