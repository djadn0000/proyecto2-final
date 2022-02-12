<?php

namespace App\Http\Controllers;

use App\Http\Requests\BlacklistFormRequest;
use App\Models\Blacklist;
use Illuminate\Http\Request;
use Carbon\Carbon;

class BlackListController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $blacklist = Blacklist::ALL();

        return view('blackList.index', compact('blacklist'));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        return view('blackList.create');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(BlacklistFormRequest $request)
    {
        $ip = gethostbyname($request->get('url'));
        if($ip == $request->get('url')){
            return redirect()->back()->with('invalid', 'URL Invalida');
        }
        $blacklist = new Blacklist();

        $blacklist->url = $request->get('url');
        $blacklist->ip = $ip;
        $blacklist->date = Carbon::now();

        $blacklist->save();

        return redirect( '/blacklists');

    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $blacklist = Blacklist::where('id', $id)->firstOrFail();;

        return view('blackList.edit', compact('blacklist'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(BlacklistFormRequest $request, $id)
    {
        $blacklist = Blacklist::findOrFail($id);

        $blacklist->url = $request->get('url');
        $blacklist->date = Carbon::now();

        $blacklist->update();

        return redirect( '/blacklists');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        $blacklist = Blacklist::findOrFail($id);

        $blacklist->delete();

        return redirect( '/blacklists');

    }
}
