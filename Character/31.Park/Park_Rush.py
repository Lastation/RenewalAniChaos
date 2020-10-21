if (f.loop[cp] == 0 && Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill"))
      {       
      MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
      MoveLocation("31.Park_Bozo", f.heroID[cp], cp, "Anywhere");
         if (cp < 3)
         {
            if (Bring(3, AtLeast, 1, f.heroID[3], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp], f.heroID[3], 3, "Anywhere");
            }
            else if (Bring(4, AtLeast, 1, f.heroID[4], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp], f.heroID[4], 4, "Anywhere");
            }
            else if (Bring(5, AtLeast, 1, f.heroID[5], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp], f.heroID[5], 5, "Anywhere");
            }

         }
         else if (cp >= 3)
         {
            if (Bring(0, AtLeast, 1, f.heroID[0], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp], f.heroID[0], 0, "Anywhere");
            }
            else if (Bring(1, AtLeast, 1, f.heroID[1], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp],f.heroID[1], 1, "Anywhere");
            }
            else if (Bring(2, AtLeast, 1, f.heroID[2], "31.Park_Bozo"))
            {
               MoveLocation(f.location[cp], f.heroID[2], 2, "Anywhere");
            }
         }
         MoveUnit(All, f.heroID[cp], cp, "Anywhere", f.location[cp]);
if (f.loop[cp] == 0)


         f.SkillWait(cp, 80);

         f.count[cp] += 1;
         f.loop[cp] = 0;
      }
