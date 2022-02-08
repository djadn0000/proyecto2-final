@extends('adminlte::page')

@section('title', 'Dashboard')

@section('content_header')
@stop

@section('content')
    <br>
    <div class="container-fluid">

        <!-- DataTales Example -->
        <div class="card shadow mb-4">
            <div class="card-header py-3">
                <div class="col-md-6 col-lg-6">
                    <h2 class="m-0 font-weight-bold text-primary"  >
                        Bienvenido {{$user->name}}
                    </h2>
                </div>

            </div>
            <div class="card-body">

                <div class="row">
                    <div class="col-md-8 col-lg-8 input-group mb-3">
                        <div class="col-md-12 col-lg-12 input-group mb-3">
                        <input type="text" name="name" id="name" class="form-control" value="{{$user->name}}" disabled >
                        </div>
                        <div class="col-md-12 col-lg-12 input-group mb-3">
                        <input type="text" name="email" id="email" class="form-control" value="{{$user->email}}" disabled>
                        </div>
                    </div>
                    <div class="col-md-4 col-lg-4 input-group mb-3" style=" border-left: solid blue; ">
                        <div class="col-md-12 col-lg-12 input-group mb-3">
                        <a href="{{url('/user/'.$user->id.'/edit')}}" >
                            <button type="button" class="btn btn-primary btn-block">Editar Usuario</button>
                        </a>
                        </div>
                        <div class="col-md-12 col-lg-12 input-group mb-3">
                        <a href="{{url('/user/password')}}" >
                            <button type="button" class="btn btn-info btn-block">Cambiar Contraseña</button>
                        </a>
                        </div>
                    </div>

                </div>

            </div>
            <div class="card-footer py-3">
                <a href="{{url('/home')}}" >
                    <button type="button" class="btn btn-warning float-right">Volver</button>
                </a>

            </div>
        </div>

    </div>
@stop

@section('css')
    <link rel="stylesheet" href="/css/admin_custom.css">
@stop

@section('js')
    <script> console.log('Hi!'); </script>
@stop

