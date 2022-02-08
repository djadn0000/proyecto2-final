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
                        Bloquear URL
                    </h2>
                </div>

            </div>
            <div class="card-body">
                <form class="" action="/blacklists/store" method="POST">
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
                        <div class="col-md-8 col-lg-8 input-group mb-3">
                            <input type="text" name="url" id="url" class="form-control" placeholder="Introduzca la URL">
                        </div>
                        <div class="col-md-4 col-lg-4 input-group mb-3">
                            <button type="submit" class="btn btn-primary">Guardar</button>
                        </div>

                    </div>
                </form>


            </div>
            <div class="card-footer py-3">
                <a href="{{url('/blacklists')}}" >
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
