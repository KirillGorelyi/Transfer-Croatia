<template>
  <div class="about-us">
    <h1>{{ $t('about_us_title') }}</h1>
    <p>{{ $t('about_us_intro') }}</p>
  </div>
</template>

<script>
export default {
  name: 'AboutUs',
  data() {
    return {
      team: [
        { id: 1, name: this.$t('team_member_name_1'), role: this.$t('team_member_role_1'), bio: this.$t('team_member_bio_1') },
      ]
    };
  }
};
</script>

<style scoped>
.about-us {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
h1, h2, h3 {
  color: #333;
}
p {
  color: #555;
  line-height: 1.6;
}
.team-member {
  margin-bottom: 20px;
}
</style>
