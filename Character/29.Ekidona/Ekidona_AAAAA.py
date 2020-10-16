import Function as f;

//0 -> X
//1 -> 활성
//2 -> 대기
var flag = 0;
var pre_flag = 0;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("JunkYardDog - Ekidona", Set);
         }

         if (f.loop[cp] % 40 == 0)
         {
            flag = 0;

            f.DotShape(cp, 8, "Zerg Devourer", 0, 0);
            if (cp < 3)
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P7);
            else if (cp >= 3)
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P8);
         }
         if (f.loop[cp] % 40 == 1)
         {
            flag = 1;

            GiveUnits(All, "Zerg Devourer", P7, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P8, "Anywhere", cp);
         }
         if (f.loop[cp] % 40 == 19)
         {
            MoveUnit(All, "Zerg Devourer", cp, "Anywhere", "[Skill]HoldPosition");
         }
         if (f.loop[cp] % 40 == 20)
         {
            flag = 2;
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 200)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         f.SkillEnd(cp);
      }

      if (flag == 1)
      {
         if (pre_flag != flag)
         {
            GiveUnits(All, "Zerg Devourer", P11, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P7, "Anywhere", cp);
            GiveUnits(All, "Zerg Devourer", P8, "Anywhere", cp);

            pre_flag = flag;
         }

         if (Bring(cp, AtLeast, 1, "Zerg Devourer", "Anywhere"))
         {
            for (var i = 0; i < 8; i++)
            {
               f.MoveLoc("Zerg Devourer", cp, 0, 0);
               GiveUnits(1, "Zerg Devourer", cp, "Anywhere", P11);

               if (i % 2 == 0) 
               {
                  f.SkillUnit(cp, 1, "80 + 1n Tom Kazansky");
                  f.SkillUnit(cp, 1, "Protoss Dark Archon");
               }
               else if (i % 2 == 1)
               {
                  f.SkillUnit(cp, 1, "80 + 1n Artanis");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
            }

            KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else
         {
            GiveUnits(All, "Zerg Devourer", P11, "Anywhere", cp);
         }

      }
      else if (flag == 2)
      {
         if (pre_flag != flag)
         {
            if (cp < 3)
            {
               GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P7);
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P7);
            }
            else if (cp >= 3)
            {
               GiveUnits(All, "Zerg Devourer", P11, "Anywhere", P8);
               GiveUnits(All, "Zerg Devourer", cp, "Anywhere", P8);
            }

            pre_flag = flag;
         }

         if (cp < 3)
         {
            if (Bring(P7, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            {
               for (var i = 0; i < 8; i++)
               {
                  f.MoveLoc("Zerg Devourer", P7, 0, 0);
                  GiveUnits(1, "Zerg Devourer", P7, "Anywhere", P11);

                  if (i % 4 == 0) 
                  {
                     f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                     f.SkillUnit(cp, 1, "60 + 1n Siege");
                     f.SkillUnit(cp, 1, "80 + 1n Tank");
                  }
                  else if (i % 4 == 1)
                  {
                     f.SkillUnit(cp, 1, "60 + 1n Danimoth");
                     f.SkillUnit(cp, 1, "60 + 1n Siege");
                     f.SkillUnit(cp, 1, "60 + 1n Archon");
                  }
                  else if (i % 4 == 2)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Wraith");
                     f.SkillUnit(cp, 1, "50 + 1n Tank");
                     f.SkillUnit(cp, 1, "80 + 1n Tank");
                  }
                  else if (i % 4 == 3)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Mojo");
                     f.SkillUnit(cp, 1, "60 + 1n Dragoon");
                     f.SkillUnit(cp, 1, "60 + 1n Archon");
                  }
               }

               KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
               Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
               Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
               Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            }
            else
            {
               GiveUnits(All, "Zerg Devourer", P11, "Anywhere", cp);
               flag = 1;
            }
         }
         else if (cp >= 3)
         {
            if (Bring(P8, AtLeast, 1, "Zerg Devourer", "Anywhere"))
            {
               for (var i = 0; i < 8; i++)
               {
                  f.MoveLoc("Zerg Devourer", P8, 0, 0);
                  GiveUnits(1, "Zerg Devourer", P8, "Anywhere", P11);

                  if (i % 4 == 0) 
                  {
                     f.SkillUnit(cp, 1, "50 + 1n Battlecruiser");
                     f.SkillUnit(cp, 1, "60 + 1n Siege");
                     f.SkillUnit(cp, 1, "80 + 1n Tank");
                  }
                  else if (i % 4 == 1)
                  {
                     f.SkillUnit(cp, 1, "60 + 1n Danimoth");
                     f.SkillUnit(cp, 1, "60 + 1n Siege");
                     f.SkillUnit(cp, 1, "60 + 1n Archon");
                  }
                  else if (i % 4 == 2)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Wraith");
                     f.SkillUnit(cp, 1, "50 + 1n Tank");
                     f.SkillUnit(cp, 1, "80 + 1n Tank");
                  }
                  else if (i % 4 == 3)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Mojo");
                     f.SkillUnit(cp, 1, "60 + 1n Dragoon");
                     f.SkillUnit(cp, 1, "60 + 1n Archon");
                  }
               }

               KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);
               KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);
               Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);
               Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
               Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
               Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            }
            else
            {
               GiveUnits(All, "Zerg Devourer", P11, "Anywhere", cp);
               flag = 1;
            }
         }

      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}