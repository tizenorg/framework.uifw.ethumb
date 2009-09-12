#ifndef __ETHUMB_CLIENT_H__
#define __ETHUMB_CLIENT_H__ 1

#ifndef EAPI
#ifdef _WIN32
# ifdef EFL_EVAS_BUILD
#  ifdef DLL_EXPORT
#   define EAPI __declspec(dllexport)
#   define GNUC_NULL_TERMINATED
#  else
#   define EAPI
#   define GNUC_NULL_TERMINATED
#  endif /* ! DLL_EXPORT */
# else
#  define EAPI __declspec(dllimport)
#  define GNUC_NULL_TERMINATED
# endif /* ! EFL_EVAS_BUILD */
#else
# ifdef __GNUC__
#  if __GNUC__ >= 4
#   define EAPI __attribute__ ((visibility("default")))
#   define GNUC_NULL_TERMINATED __attribute__((__sentinel__))
#  else
#   define EAPI
#  define GNUC_NULL_TERMINATED
#  endif
# else
#  define EAPI
#  define GNUC_NULL_TERMINATED
# endif
#endif /* ! _WIN32 */
#endif /* EAPI */

#include <Ethumb.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct _Ethumb_Client Ethumb_Client;
typedef void (*Ethumb_Client_Connect_Cb)(void *data, Ethumb_Client *client, Eina_Bool success);
typedef void (*Ethumb_Client_Die_Cb)(void *data, Ethumb_Client *client);
typedef void (*Ethumb_Client_Generate_Cb)(void *data, Ethumb_Client *client, int id, const char *file, const char *key, const char *thumb_path, const char *thumb_key, Eina_Bool success);
typedef void (*Ethumb_Client_Generate_Cancel_Cb)(void *data, Eina_Bool success);

EAPI int ethumb_client_init(void);
EAPI int ethumb_client_shutdown(void);

EAPI Ethumb_Client * ethumb_client_connect(Ethumb_Client_Connect_Cb connect_cb, const void *data, Eina_Free_Cb free_data);
EAPI void ethumb_client_disconnect(Ethumb_Client *client);
EAPI void ethumb_client_on_server_die_callback_set(Ethumb_Client *client, Ethumb_Client_Die_Cb server_die_cb, const void *data, Eina_Free_Cb free_data);

EAPI void ethumb_client_fdo_set(Ethumb_Client *client, Ethumb_Thumb_FDO_Size s);
EAPI void ethumb_client_size_set(Ethumb_Client *client, int tw, int th);
EAPI void ethumb_client_size_get(const Ethumb_Client *client, int *tw, int *th);
EAPI void ethumb_client_format_set(Ethumb_Client *client, Ethumb_Thumb_Format f);
EAPI Ethumb_Thumb_Format ethumb_client_format_get(const Ethumb_Client *client);
EAPI void ethumb_client_aspect_set(Ethumb_Client *client, Ethumb_Thumb_Aspect a);
EAPI Ethumb_Thumb_Aspect ethumb_client_aspect_get(const Ethumb_Client *client);
EAPI void ethumb_client_crop_align_set(Ethumb_Client *client, float x, float y);
EAPI void ethumb_client_crop_align_get(const Ethumb_Client *client, float *x, float *y);
EAPI void ethumb_client_quality_set(Ethumb_Client *client, int quality);
EAPI int ethumb_client_quality_get(const Ethumb_Client *client);
EAPI void ethumb_client_compress_set(Ethumb_Client *client, int compress);
EAPI int ethumb_client_compress_get(const Ethumb_Client *client);
EAPI Eina_Bool ethumb_client_frame_set(Ethumb_Client *client, const char *file, const char *group, const char *swallow);
EAPI void ethumb_client_dir_path_set(Ethumb_Client *client, const char *path);
EAPI const char * ethumb_client_dir_path_get(const Ethumb_Client *client);
EAPI void ethumb_client_category_set(Ethumb_Client *client, const char *category);
EAPI const char * ethumb_client_category_get(const Ethumb_Client *client);
EAPI void ethumb_client_video_time_set(Ethumb_Client *client, float time);
EAPI void ethumb_client_video_start_set(Ethumb_Client *client, float start);
EAPI void ethumb_client_video_interval_set(Ethumb_Client *client, float interval);
EAPI void ethumb_client_video_ntimes_set(Ethumb_Client *client, int ntimes);
EAPI void ethumb_client_video_fps_set(Ethumb_Client *client, int fps);
EAPI void ethumb_client_document_page_set(Ethumb_Client *client, int page);

EAPI void ethumb_client_ethumb_setup(Ethumb_Client *client);

EAPI Eina_Bool ethumb_client_file_set(Ethumb_Client *client, const char *path, const char *key);
EAPI void ethumb_client_file_get(Ethumb_Client *client, const char **path, const char **key);
EAPI void ethumb_client_file_free(Ethumb_Client *client);

EAPI void ethumb_client_thumb_path_set(Ethumb_Client *client, const char *path, const char *key);
EAPI void ethumb_client_thumb_path_get(Ethumb_Client *client, const char **path, const char **key);
EAPI Eina_Bool ethumb_client_thumb_exists(Ethumb_Client *client);
EAPI int  ethumb_client_generate(Ethumb_Client *client, Ethumb_Client_Generate_Cb generated_cb, const void *data, Eina_Free_Cb free_data);
EAPI void ethumb_client_generate_cancel(Ethumb_Client *client, int id, Ethumb_Client_Generate_Cancel_Cb cancel_cb, const void *data, Eina_Free_Cb free_data);
EAPI void ethumb_client_generate_cancel_all(Ethumb_Client *client);

#ifdef __cplusplus
}
#endif
#endif /* __ETHUMB_CLIENT_H__ */
