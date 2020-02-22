/* Created by Language version: 7.5.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__Gfluctp
#define _nrn_initial _nrn_initial__Gfluctp
#define nrn_cur _nrn_cur__Gfluctp
#define _nrn_current _nrn_current__Gfluctp
#define nrn_jacob _nrn_jacob__Gfluctp
#define nrn_state _nrn_state__Gfluctp
#define _net_receive _net_receive__Gfluctp 
#define noiseFromRandom123 noiseFromRandom123__Gfluctp 
#define oup oup__Gfluctp 
#define seeds123 seeds123__Gfluctp 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define E_e _p[0]
#define E_i _p[1]
#define g_e0 _p[2]
#define g_i0 _p[3]
#define std_e _p[4]
#define std_i _p[5]
#define tau_e _p[6]
#define tau_i _p[7]
#define seed1 _p[8]
#define seed2 _p[9]
#define seed3 _p[10]
#define i _p[11]
#define g_e _p[12]
#define g_i _p[13]
#define g_e1 _p[14]
#define g_i1 _p[15]
#define D_e _p[16]
#define D_i _p[17]
#define rv _p[18]
#define id _p[19]
#define exp_e _p[20]
#define exp_i _p[21]
#define amp_e _p[22]
#define amp_i _p[23]
#define v _p[24]
#define _g _p[25]
#define _nd_area  *_ppvar[0]._pval
#define internalpointer	*_ppvar[2]._pval
#define _p_internalpointer	_ppvar[2]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  2;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 /* declaration of user functions */
 static double _hoc_noiseFromRandom123();
 static double _hoc_oup();
 static double _hoc_rand();
 static double _hoc_seeds123();
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 extern Prop* nrn_point_prop_;
 static int _pointtype;
 static void* _hoc_create_pnt(_ho) Object* _ho; { void* create_point_process();
 return create_point_process(_pointtype, _ho);
}
 static void _hoc_destroy_pnt();
 static double _hoc_loc_pnt(_vptr) void* _vptr; {double loc_point_process();
 return loc_point_process(_pointtype, _vptr);
}
 static double _hoc_has_loc(_vptr) void* _vptr; {double has_loc_point();
 return has_loc_point(_vptr);
}
 static double _hoc_get_loc_pnt(_vptr)void* _vptr; {
 double get_loc_point_process(); return (get_loc_point_process(_vptr));
}
 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata(void* _vptr) { Prop* _prop;
 _prop = ((Point_process*)_vptr)->_prop;
   _setdata(_prop);
 }
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 0,0
};
 static Member_func _member_func[] = {
 "loc", _hoc_loc_pnt,
 "has_loc", _hoc_has_loc,
 "get_loc", _hoc_get_loc_pnt,
 "noiseFromRandom123", _hoc_noiseFromRandom123,
 "oup", _hoc_oup,
 "rand", _hoc_rand,
 "seeds123", _hoc_seeds123,
 0, 0
};
#define rand rand_Gfluctp
 extern double rand( _threadargsproto_ );
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "E_e", "mV",
 "E_i", "mV",
 "g_e0", "umho",
 "g_i0", "umho",
 "std_e", "umho",
 "std_i", "umho",
 "tau_e", "ms",
 "tau_i", "ms",
 "i", "nA",
 "g_e", "umho",
 "g_i", "umho",
 "g_e1", "umho",
 "g_i1", "umho",
 "D_e", "umho umho /ms",
 "D_i", "umho umho /ms",
 0,0
};
 static double delta_t = 0.01;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 static void _hoc_destroy_pnt(_vptr) void* _vptr; {
   destroy_point_process(_vptr);
}
 
static int _ode_count(int);
 static void _constructor(Prop*);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.5.0",
"Gfluctp",
 "E_e",
 "E_i",
 "g_e0",
 "g_i0",
 "std_e",
 "std_i",
 "tau_e",
 "tau_i",
 "seed1",
 "seed2",
 "seed3",
 0,
 "i",
 "g_e",
 "g_i",
 "g_e1",
 "g_i1",
 "D_e",
 "D_i",
 "rv",
 "id",
 0,
 0,
 "internalpointer",
 0};
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
  if (nrn_point_prop_) {
	_prop->_alloc_seq = nrn_point_prop_->_alloc_seq;
	_p = nrn_point_prop_->param;
	_ppvar = nrn_point_prop_->dparam;
 }else{
 	_p = nrn_prop_data_alloc(_mechtype, 26, _prop);
 	/*initialize range parameters*/
 	E_e = 0;
 	E_i = -75;
 	g_e0 = 0.0121;
 	g_i0 = 0.0573;
 	std_e = 0.003;
 	std_i = 0.0066;
 	tau_e = 2.728;
 	tau_i = 10.49;
 	seed1 = 1;
 	seed2 = 1;
 	seed3 = 1;
  }
 	_prop->param = _p;
 	_prop->param_size = 26;
  if (!nrn_point_prop_) {
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 3, _prop);
  }
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 if (!nrn_point_prop_) {_constructor(_prop);}
 
}
 static void _initlists();
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _Gfluctp_reg() {
	int _vectorized = 1;
  _initlists();
 	_pointtype = point_register_mech(_mechanism,
	 nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init,
	 hoc_nrnpointerindex, 1,
	 _hoc_create_pnt, _hoc_destroy_pnt, _member_func);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
  hoc_register_prop_size(_mechtype, 26, 3);
  hoc_register_dparam_semantics(_mechtype, 0, "area");
  hoc_register_dparam_semantics(_mechtype, 1, "pntproc");
  hoc_register_dparam_semantics(_mechtype, 2, "pointer");
 	hoc_register_cvode(_mechtype, _ode_count, 0, 0, 0);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 Gfluctp /home/craig/Documents/Repos/EEE_network/x86_64/Gfluctp.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "Fluctuating conductances with parallel random streams";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int noiseFromRandom123(_threadargsproto_);
static int oup(_threadargsproto_);
static int seeds123(_threadargsprotocomma_ double, double, double);
 
/*VERBATIM*/
#include "nrnran123.h"
 
static int  oup ( _threadargsproto_ ) {
   if ( tau_e  != 0.0 ) {
     g_e1 = exp_e * g_e1 + amp_e * rand ( _threadargs_ ) ;
     }
   if ( tau_i  != 0.0 ) {
     g_i1 = exp_i * g_i1 + amp_i * rand ( _threadargs_ ) ;
     }
    return 0; }
 
static double _hoc_oup(void* _vptr) {
 double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   _p = ((Point_process*)_vptr)->_prop->param;
  _ppvar = ((Point_process*)_vptr)->_prop->dparam;
  _thread = _extcall_thread;
  _nt = (_NrnThread*)((Point_process*)_vptr)->_vnt;
 _r = 1.;
 oup ( _p, _ppvar, _thread, _nt );
 return(_r);
}
 
double rand ( _threadargsproto_ ) {
   double _lrand;
 
/*VERBATIM*/
  // Supports separate independent but reproducible streams for eaach instance. However, the corresponding hoc Random distribution MUST be set to Random.negexp(1)
  if (_p_internalpointer) {
     // _lrand = nrnran123_negexp((nrnran123_State*)_p_internalpointer);
     _lrand = nrnran123_normal((nrnran123_State*)_p_internalpointer);
  }
 
return _lrand;
 }
 
static double _hoc_rand(void* _vptr) {
 double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   _p = ((Point_process*)_vptr)->_prop->param;
  _ppvar = ((Point_process*)_vptr)->_prop->dparam;
  _thread = _extcall_thread;
  _nt = (_NrnThread*)((Point_process*)_vptr)->_vnt;
 _r =  rand ( _p, _ppvar, _thread, _nt );
 return(_r);
}
 
static int  seeds123 ( _threadargsprotocomma_ double _la , double _lb , double _lc ) {
   
/*VERBATIM*/
  nrnran123_State** pv = (nrnran123_State**)(&_p_internalpointer);
  if (*pv) {
    nrnran123_deletestream(*pv);
    *pv = (nrnran123_State*)0;
  }
  *pv = nrnran123_newstream3(_la, _lb, _lc);
  return 0; }
 
static double _hoc_seeds123(void* _vptr) {
 double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   _p = ((Point_process*)_vptr)->_prop->param;
  _ppvar = ((Point_process*)_vptr)->_prop->dparam;
  _thread = _extcall_thread;
  _nt = (_NrnThread*)((Point_process*)_vptr)->_vnt;
 _r = 1.;
 seeds123 ( _p, _ppvar, _thread, _nt, *getarg(1) , *getarg(2) , *getarg(3) );
 return(_r);
}
 
static int  noiseFromRandom123 ( _threadargsproto_ ) {
   
/*VERBATIM*/
  nrnran123_State** pv = (nrnran123_State**)(&_p_internalpointer);
  if (*pv) {
    nrnran123_deletestream(*pv);
    *pv = (nrnran123_State*)0;
  }
  if (ifarg(3)) {
    *pv = nrnran123_newstream3((uint32_t)*getarg(1), (uint32_t)*getarg(2), (uint32_t)*getarg(3));
  } else if (ifarg(2)) {
    *pv = nrnran123_newstream((uint32_t)*getarg(1), (uint32_t)*getarg(2));
  } else if (ifarg(1)) {
    *pv = nrnran123_newstream((uint32_t)*getarg(1), (uint32_t)0);
  } else {
    *pv = nrnran123_newstream3((uint32_t)seed1, (uint32_t)seed2, (uint32_t)seed3);
  }
  return 0; }
 
static double _hoc_noiseFromRandom123(void* _vptr) {
 double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   _p = ((Point_process*)_vptr)->_prop->param;
  _ppvar = ((Point_process*)_vptr)->_prop->dparam;
  _thread = _extcall_thread;
  _nt = (_NrnThread*)((Point_process*)_vptr)->_vnt;
 _r = 1.;
 noiseFromRandom123 ( _p, _ppvar, _thread, _nt );
 return(_r);
}
 
static int _ode_count(int _type){ hoc_execerror("Gfluctp", "cannot be used with CVODE"); return 0;}
 
static void _constructor(Prop* _prop) {
	double* _p; Datum* _ppvar; Datum* _thread;
	_thread = (Datum*)0;
	_p = _prop->param; _ppvar = _prop->dparam;
{
 {
   
/*VERBATIM*/
  id=ifarg(2)?(int)*getarg(2):17.2;
 }
 
}
}

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
 {
   seeds123 ( _threadargscomma_ seed1 , seed2 , seed3 ) ;
   
/*VERBATIM*/
  // only this style initializes the stream on finitialize
  if (_p_internalpointer) { nrnran123_setseq((nrnran123_State*)_p_internalpointer, 0, 0); }
 g_e1 = 0.0 ;
   g_i1 = 0.0 ;
   if ( tau_e  != 0.0 ) {
     D_e = 2.0 * std_e * std_e / tau_e ;
     exp_e = exp ( - dt / tau_e ) ;
     amp_e = std_e * sqrt ( ( 1.0 - exp ( - 2.0 * dt / tau_e ) ) ) ;
     }
   if ( tau_i  != 0.0 ) {
     D_i = 2.0 * std_i * std_i / tau_i ;
     exp_i = exp ( - dt / tau_i ) ;
     amp_i = std_i * sqrt ( ( 1.0 - exp ( - 2.0 * dt / tau_i ) ) ) ;
     }
   }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
 initmodel(_p, _ppvar, _thread, _nt);
}
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   if ( tau_e  == 0.0 ) {
     g_e = std_e * rand ( _threadargs_ ) ;
     }
   if ( tau_i  == 0.0 ) {
     g_i = std_i * rand ( _threadargs_ ) ;
     }
   g_e = g_e0 + g_e1 ;
   if ( g_e < 0.0 ) {
     g_e = 0.0 ;
     }
   g_i = g_i0 + g_i1 ;
   if ( g_i < 0.0 ) {
     g_i = 0.0 ;
     }
   i = g_e * ( v - E_e ) + g_i * ( v - E_i ) ;
   }
 _current += i;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
 	}
 _g = (_g - _rhs)/.001;
 _g *=  1.e2/(_nd_area);
 _rhs *= 1.e2/(_nd_area);
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}
 
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
 {  { oup(_p, _ppvar, _thread, _nt); }
  }}}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif
