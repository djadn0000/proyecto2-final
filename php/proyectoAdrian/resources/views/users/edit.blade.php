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
                        Editar Usuario: {{$user->name}}
                    </h2>
                </div>

            </div>
            <div class="card-body">
                <form class="" action="{{url('/user/update/'.$user->id)}}" method="POST">
                    @method('PATCH')
                    @csrf
                    @if ($errors->any())
                        <div class="alert alert-danger">
                            <ul>
                                @foreach ($errors->all() as $error)
                                    <li>{{ $error }}</li>
                                @endforeach
                            </ul>
                        </div>
                    @endif
                    <div class="row">
                        <div class="col-md-5 col-lg-5 input-group mb-3">
                            <input type="text" name="name" id="name" class="form-control" value="{{$user->name}}" >
                        </div>
                        <div class="col-md-5 col-lg-5 input-group mb-3">
                            <input type="text" name="email" id="email" class="form-control" value="{{$user->email}}">
                        </div>

                        <div class="col-md-2 col-lg-2 input-group mb-3">

                            <button type="submit" class="btn btn-primary btn-block">Guardar Cambios</button>

                        </div>



                    </div>
                </form>
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


