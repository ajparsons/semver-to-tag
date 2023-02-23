# Semver to tag

Version: 0.1.0



Given a valid Semver, update the tags on the github repo.

## Usage

```yaml

# It is better practice to use the SHA hash of this tag rather than the tag itself.
- uses: ajparsons/semver-to-tag@v0
  id: example-step 
  with:
    semver: '' 
    update_tags: 'true'  # default

```


## Inputs

### semver



Valid semver




### update_tags



true or false, update the github repository tags

Default: true




## Outputs

### tag_exists

Boolean of if all tags already existed.


### semver_tags

Space seperated semver tags


### major_tag

Major tag version (e.g. v1)


### minor_tag

Major tag version (e.g. v1.1)


### patch_tag

Major tag version (e.g. v1.1.1)


