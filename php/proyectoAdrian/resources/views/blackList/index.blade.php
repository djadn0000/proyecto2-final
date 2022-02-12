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
                <div class="row">
                    <div class="col-md-6 col-lg-6">
                        <h2 class="m-0 font-weight-bold text-primary"  >
                            Lista de URLs Bloqueadas
                        </h2>
                    </div>
                    <div class="col-md-6 col-lg-6">
                        <a href="{{url('/blacklists/create')}}">
                            <button type="button" class="btn btn-success float-right">Bloquear Nueva URL</button>
                        </a>
                    </div>
                </div>
            </div>
            <div class="card-body">
                @if ($message = Session::get('success'))
                    <div class="alert alert-success alert-block">
                        <button type="button" class="close" data-dismiss="alert">×</button>
                        <strong>{{ $message }}</strong>
                    </div>
                @endif

                <table class="table table-bordered" id="tablaSolicitudes" width="100%" cellspacing="0" style="text-align: center" >
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>URL</th>
                        <th>IP</th>
                        <th>Fecha</th>
                        <th>Opciones</th>
                    </tr>
                    </thead>
                    <!-- <tfoot>
                     <tr>
                         <th>ID</th>
                         <th>Cliente</th>
                         <th>Monto</th>
                         <th>Incorporación</th>
                         <th>Estado</th>
                         <th>Opciones</th>
                     </tr>
                     </tfoot>-->
                    <tbody>

                    @foreach($blacklist as $black)
                        @include('blackList.modal_delete')
                        <tr>
                            <td>{{$black->id}}</td>

                            <td>{{$black->url}}</td>
                            <td>{{$black->ip}}</td>
                            <td>{{$black->date}}</td>


                            <td>


                                <a href="{{url('/blacklists/'.$black->id.'/edit')}}" title="Actualizar URL">
                                    <button type="button" class="btn btn-primary">
                                        <i class="far fa-edit"></i>
                                    </button>
                                </a>

                                <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#modalDestroy-{{$black->id}}">
                                    <i class="far fa-trash-alt"></i>
                                </button>


                            </td>

                        </tr>

                    @endforeach

                    </tbody>
                </table>
            </div>
        </div>

    </div>
@stop

@section('css')

    <link  rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.22/css/dataTables.bootstrap4.min.css" >
    <link  rel="stylesheet" href="https://cdn.datatables.net/responsive/2.2.6/css/responsive.bootstrap4.min.css">
@stop

@section('js')
    <script> console.log('Hi!'); </script>
    <script src="https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.22/js/dataTables.bootstrap4.min.js"></script>
    <script src="https://cdn.datatables.net/responsive/2.2.6/js/dataTables.responsive.min.js"></script>
    <script src="https://cdn.datatables.net/responsive/2.2.6/js/responsive.bootstrap4.min.js"></script>

    <script>
        $('#tablaSolicitudes').DataTable({
            responsive : true,
            autoWidth : false,
            "language": {
                "lengthMenu": "Mostrar " +
                    `<select class ="custom-select custom-select-sm form-control form-contorl-sm" >
                                       <option value ='10'>10</option>
                                       <option value ='25'>25</option>
                                       <option value ='50'>50</option>
                                       <option value ='100'>100</option>
                                       <option value ='-1' >Todos</option>
                                        </select>` +
                    " Registros por pagina",
                "zeroRecords": "Nada encontrado - Disculpa",
                "info": "Mostrando la pagina _PAGE_ de _PAGES_",
                "infoEmpty": "No records available",
                "infoFiltered": "(Filtrados de _MAX_ registros totales)",
                "search": "Buscar:",
                "paginate":{
                    "next": "Siguiente",
                    "previous": "Anterior"
                }

            }
        });

    </script>
@stop
