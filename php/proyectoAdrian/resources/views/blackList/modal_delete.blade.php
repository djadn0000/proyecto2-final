<div class="modal fade" id="modalDestroy-{{$black->id}}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Eliminar URL</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                ¿Desea eliminar esta URL?
            </div>
            <div class="modal-footer">
                <a href="{{url('/blacklists')}}">
                    <button type="button" class="btn btn-danger">Cancelar</button>
                </a>
                <form id="form-eliminar" class="" action="{{url('/blacklists/'. $black->id)}}" method="POST">
                    @method('delete')
                    @csrf
                    <button type="submit" class="btn btn-primary" id="botonEliminarMensaje">Sí</button>
                </form>
            </div>

        </div>
    </div>
</div>


