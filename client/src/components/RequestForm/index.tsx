import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

const UploadSchema = Yup.object().shape({
    videoUrl: Yup.string().url('Invalid URL').required('Required'),
});

type Props = {
    onSubmit: (url: string) => void;
};

const RequestForm: React.FC<Props> = ({ onSubmit }) => {
    return (
        <Formik
            initialValues={{ videoUrl: '' }}
            validationSchema={UploadSchema}
            onSubmit={(values) => {
                onSubmit(values.videoUrl);
            }}
        >
            {({ errors, touched }) => (
                <Form className="space-y-4 p-4">
                    <label className="block text-sm font-medium">
                        YouTube Video URL
                    </label>
                    <Field
                        name="videoUrl"
                        type="url"
                        className="w-full p-2 border rounded"
                        placeholder="https://www.youtube.com/watch?v=..."
                    />
                    {errors.videoUrl && touched.videoUrl ? (
                        <div className="text-red-500 text-sm">
                            {errors.videoUrl}
                        </div>
                    ) : null}
                    <button
                        type="submit"
                        className="bg-blue-600 text-white px-4 py-2 rounded"
                    >
                        Summarize
                    </button>
                </Form>
            )}
        </Formik>
    );
};

export default RequestForm;
