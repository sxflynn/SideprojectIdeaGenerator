import { Box, Button, MultiSelect } from "@mantine/core";
import { useForm } from "@mantine/form";

export function Form() {
  const form = useForm({
    initialValues: {
      knownTech: [],
      unknownTech: [],
      topics: [],
    },
  });

  return (
    <Box>
      <form onSubmit={form.onSubmit((values) => console.log(values))}>
        {/* <TextInput label="Tech you know" {...form.getInputProps("knownTech")} /> */}
        <MultiSelect
      label="Tech you know"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("knownTech")}
    />
        <MultiSelect
      label="Tech you don't know"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("unknownTech")}
    />
        <MultiSelect
      label="Topics you like"
      data={['React', 'Angular', 'Vue', 'Svelte']}
      searchable
      {...form.getInputProps("topics")}
    />
      <Button type="submit">Submit</Button>
      
  

      </form>
    </Box>
  );
}
